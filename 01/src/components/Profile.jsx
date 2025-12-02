import "./Profile.css";

export default function Header() {
  // 프로필 데이터 (객체)
  const profile = {
    name: "김철수",
    age: 28,
    job: "프론트엔드 개발자",
    skills: ["JavaScript", "React", "TypeScript", "CSS"],
    image: "https://via.placeholder.com/150",
  };

  return (
    <div className="app">
      <div className="profile-card">
        <img
          className="profile-image"
          src={profile.image}
          alt={profile.name}
        />
        <h1 className="profile-name">{profile.name}</h1>
        <p className="profile-job">{profile.job}</p>
        <p className="profile-age">{profile.age}세</p>

        <h2 className="skills-title">Skills</h2>
        <ul className="skills-list">
          {profile.skills.map((skill) => (
            <li key={skill} className="skill-chip">
              {skill}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
